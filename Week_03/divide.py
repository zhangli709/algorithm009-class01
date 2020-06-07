
# 分治代码模板

def divide_conquer(problem, param1, param2, ...):

    # recursion terminator  1. 返回条件
    if problem is None:
        print_result
        return

    # prepare data 2.
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems  3. 处理当前逻辑
    subresult1 = self.divede_conquer(subproblems[0], p1, ...)
    subresult2 = self.divede_conquer(subproblems[1], p1, ...)
    subresult3 = self.divede_conquer(subproblems[2], p1, ...)
    ...

    # process and generate the final result  3.
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states