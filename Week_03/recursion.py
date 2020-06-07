

# 递归模板

# Python
def recursion(level, param1, param2, ...):
    # recursion terminator  1. 递归终结条件
    if level > MAX_LEVEL:
        process_result
        return
    # process logic in current level  2 处理当前逻辑
    process(level, data...)
    # drill down  3 下探到下一层
    self.recursion(level + 1, p1, ...)

    # 4. 清理当前层
    # reverse the current level status if needed

