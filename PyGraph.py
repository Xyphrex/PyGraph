def sub_x(x):
    evaluation = []
    for i in equation:
        evaluation.append(i)
    for j in evaluation:
        index = evaluation.index(j)
        if j == "x" or j == "X":
            if evaluation[index - 1].isnumeric() and not index == 0:
                evaluation.insert(index,"*")
                index += 1
            evaluation[index] = "(" + str(x) + ")"
        elif j == "^":
                evaluation[index] = "**"
    return evaluation

def add_space(num):
    str_number = str(num)
    if num >= 0 and num < 10:
        str_number += "  "
    elif num >= 10 or (num < 0 and num > -10):
        str_number += " "
    return str_number

while True:
    while True:
        try:
            domain = input("Enter domain of graph: ")
            domain = int(domain)
            if domain >= 100 or domain <= -100:
                domain = 99
            domain = abs(domain)
            d_1 = round(domain - (domain * 1.5))
            d_2 = round(domain - (domain / 2) + 1)
            domain += 1
            break
        except:
            print("Please enter a valid domain.")
    rows = []
    for i in range(domain):
        row = [add_space(i+d_1)]
        for i in range(domain):
            if i == abs(d_1):
                row.append(" | ")
            else:
                row.append("   ")
        rows.append(row)
    rows.reverse()
    final_row = ["   "]
    for i in range(d_1,d_2):
        string = add_space(i)
        if string == "-1 ":
            string += " "
        final_row.append(string)
    rows.append(final_row)
    y_points = []
    equation = input("\nEnter equation of line: ")
    equation = equation.replace(" ", "")
    equation = list(equation)
    try:
        equation.remove("y")
        equation.remove("=")
    except:
        pass
                
    for i in range(d_1,d_2):
        try:
            y_points.append(round(eval("".join(sub_x(i)))))
        except:
            y_points.append("N/A")

    for i in range(domain):
        if rows[i][0] == "0  ":
            for k in range(len(rows[i])-1):
                rows[i][k+1] = "---"
        for j in range(domain):
            if y_points[j] == int(rows[i][0]):
                rows[i][j+1] = " # "
    for i in rows:
            string = ""
            for j in i:
                    string += j
            print(string)
