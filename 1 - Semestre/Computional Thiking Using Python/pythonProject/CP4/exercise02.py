def main():
    list_employees = []

    for i in range(10):
        salary = float(input(f"Digite o salario do funcionario {1+i}: "))
        total_sales = float(input(f"Digite o total de vendas do funcionario {1+i}: "))
        list_employees.append({
            "cod": 1+i,
            "salary": salary,
            "total_sales": total_sales
        })

    list_salaryWithBonus = list(map(lambda x: x["salary"]*1.2 if x["total_sales"] >= 5000 else x["salary"]*1.1, list_employees))

    print(list_salaryWithBonus)

if __name__ == '__main__':
    main()