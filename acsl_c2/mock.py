def truncate_html(html: str, max_len: int) -> str:
    i = 0
    retval = ""
    stack = []  # tags
    close_tag_len = 0
    while i < len(html):
        if html[i] == "<":
            end_idx = html.find(">", i)
            if end_idx == -1:
                if len(retval) + 1 + close_tag_len > max_len:
                    break
                else:
                    retval += html[i]
                    i += 1
            else:
                tag_content = html[i + 1 : end_idx]
                full_tag = html[i : end_idx + 1]
                # print(f"tag_content = {tag_content} full_tag = {full_tag}")
                if tag_content.startswith("/"):
                    # closing a tag
                    tag_name = tag_content[1:].strip()
                    if stack and stack[-1] == tag_name:
                        stack.pop()
                    # else silent failure
                    retval += full_tag
                    close_tag_len -= 3 + len(tag_content)
                else:
                    # Get ONLY the tag name (e.g., "p" from "p class='foo'")
                    tag_name = tag_content.split()[0]
                    actual_close_len = len(tag_name) + 3
                    if (
                        len(retval)
                        + len(full_tag)  # this one
                        + actual_close_len  # closing part
                        + close_tag_len  # others we need to close
                        > max_len
                    ):
                        # this will push us over. so close tags and return.
                        break
                    # Update what we need to close
                    stack.append(tag_name)
                    close_tag_len += actual_close_len
                    # print this open
                    retval += full_tag
                i = end_idx + 1
                # print(f"i is now {i}")
        else:
            if len(retval) + 1 + close_tag_len <= max_len:
                retval += html[i]
                i += 1
            else:
                break
    while stack:
        tag = stack.pop()
        retval += f"</{tag}>"
    return retval


# --- Test Case ---
input_str: str = (
    "<p>The <b>quick</b> brown <i>fox</i> jumps over a lazy dog.</p>"
)
limit: int = 30
result = truncate_html(input_str, limit)

print(f"Target Limit: {limit}")
print(f"Result:       {result}")
print(f"Result Len:   {len(result)}")
