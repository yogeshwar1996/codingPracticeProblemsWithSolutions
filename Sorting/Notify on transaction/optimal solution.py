def calculate_median(
    expense_frequency_list, no_of_trailing_days
):
    # We calculate the median of the trailing days based on sum of frequencies of the expenses
    # If the number of trailing days is odd
    # then we return expense for which sum of frequencies of the expenses >= (no_of_trailing_days // 2) + 1
    # If the number of trailing days is even then
    # As we sum frequencies if sum > (no_of_trailing_days // 2) then the corsp expense is the median
    # If sum == (no_of_trailing_days // 2) the corsp expense is the first middle element
    # and we find another middle element by iterating over the expenses and finding the first non-zero frequency to get second middle element
    # and median will be (expense_middle1 + expense_middle2) / 2

    # If the number of trailing days is even then we return the average of the two middle elements
    if no_of_trailing_days % 2 == 0: 
        sum_of_frequencies = 0
        for expense in range(201):
            frequency_of_expense = expense_frequency_list[expense]
            sum_of_frequencies += frequency_of_expense

            if sum_of_frequencies == (no_of_trailing_days // 2):
                median_expense1 = expense
                for expenditure in range(median_expense1+1, 201):
                    if expense_frequency_list[expenditure]:
                        median_expense2 = expenditure
                        return (median_expense1 + median_expense2) / 2
            elif sum_of_frequencies > (no_of_trailing_days // 2):
                return expense

    else:
        sum_of_frequencies = 0
        for expense in range(201):
            frequency_of_expense = expense_frequency_list[expense]
            sum_of_frequencies += frequency_of_expense

            if sum_of_frequencies >= (no_of_trailing_days // 2) + 1:

                return expense


def activityNotifications(list_of_expenses, no_of_trailing_days):
    # Since list_of_expenses value is going to lie between 1-200 we will initialize an array of size 201
    print('No. of trailing days ', no_of_trailing_days)
    expense_frequency_list = [0] * 201
    notifications = 0
    total_days = len(list_of_expenses)

    # We iterate over the expenses of the trailing days and increment the frequency of the corsp expenses
    for i in range(no_of_trailing_days):
        expense = list_of_expenses[i]
        expense_frequency_list[expense] += 1

    # Now we start from the d day till the end of the list_of_expenses list
    for i in range(no_of_trailing_days, total_days):
        # We calculate the median of the trailing days
        current_expense = list_of_expenses[i]
        median = calculate_median(expense_frequency_list, no_of_trailing_days)
        if current_expense >= 2 * median:
            notifications += 1

        # We remove the first expense from the trailing days and add the new expense by adjusting their frequencies
        first_expense_in_trailing_days = list_of_expenses[i - no_of_trailing_days]
        expense_frequency_list[first_expense_in_trailing_days] -= 1
        expense_frequency_list[current_expense] += 1

    return notifications


if __name__ == "__main__":
    d = int(input())

    list_of_expenses = list(map(int, input().rstrip().split()))

    result = activityNotifications(list_of_expenses, d)
