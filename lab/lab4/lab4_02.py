# 3.2 Program generating housing occupancy report

def get_data():
    """Get occupancy data from user input"""
    
    occupancy_data = []
    for i in range(8):
        if i < 7:
            prompt = f'Provide the number of houses with {i} Occupancy: '
        else:
            prompt = 'Provide the number of houses with 6+ Occupancy: '
        occupancy_data.append(int(input(prompt)))
    return tuple(occupancy_data)


def cal_percentage(*occupancy_counts):
    """Calculate percentages for each occupancy category"""

    total_houses = sum(occupancy_counts[:7])  # Exclude 6+ from total
    percentages = []
    for count in occupancy_counts:
        percentage = (count / total_houses) * 100 if total_houses > 0 else 0
        percentages.append(percentage)
    return tuple(percentages)


def display_result(counts, percentages):
    """Display the census report"""

    labels = ['0', '1', '2', '3', '4', '5', '6', '6+']
    print(f"{'Occupancy':<12} {'Houses':<10} {'Percentage':<12}")
    print("-" * 34)
    for label, count, percentage in zip(labels, counts, percentages):
        print(f"{label:<12} {count:<10} {percentage:>10.2f}%")


if __name__ == "__main__":
    occupancy_counts = get_data()
    percentages = cal_percentage(*occupancy_counts)
    display_result(occupancy_counts, percentages)
