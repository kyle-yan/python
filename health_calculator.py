def health_calculator(age, apple_ate, cigar_smoked):
    answer = (100 - age) + (apple_ate * 3.5) - (cigar_smoked * 2)
    print(answer)

kyle_date = [25, 1, 0]

health_calculator(kyle_date[0], kyle_date[1], kyle_date[2])
health_calculator(*kyle_date)
