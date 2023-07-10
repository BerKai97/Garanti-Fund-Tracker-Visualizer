from models import Fund
import matplotlib.pyplot as plt
import numpy as np
import json


def get_funds_of_file(fund_file:str):
    with open(fund_file, encoding="utf-8") as f:
        json_data = json.load(f)

    funds: list[Fund] = []
    for fund in json_data:
        funds.append(Fund(fund))
    return funds

def get_funds_from_folder(folder:str):
    funds = []
    for i in range(1, 4):
        funds.extend(get_funds_of_file(f"{folder}/data{i}.json"))
    return funds

# Visualize profit/loss
def visualize_profit_loss():
    funds = get_funds_of_file("data.json")
    sorted_funds = sorted(funds, key=lambda fund: fund.profit_loss, reverse=True)

    fund_names = [fund.fund_name for fund in sorted_funds]
    profit_loss_values = [fund.profit_loss for fund in sorted_funds]

    # Plotting
    plt.figure(figsize=(16, 9))
    plt.bar(fund_names, profit_loss_values, color=np.where(np.array(profit_loss_values) >= 0, 'green', 'red'))
    plt.xlabel("Fund")
    plt.ylabel("Profit/Loss (TL)")
    plt.title("Fund Profit/Loss")
    plt.xticks(rotation=45)
    # plt.grid(True)
    plt.yticks(np.arange(min(profit_loss_values), max(profit_loss_values), 500))
    
    # Total profit/loss
    total_profit_loss = sum(profit_loss_values)
    plt.legend([f"Total Profit/Loss: {total_profit_loss:.2f} TL"])


    plt.tight_layout()
    plt.show()

def visualize_profit_amount_ratio():
    funds = get_funds_of_file("data.json")
    sorted_funds = sorted(funds, key=lambda fund: fund.profit_loss / fund.amount, reverse=True)

    fund_names = [fund.fund_name for fund in sorted_funds]
    real_profit_loss_values = [fund.profit_loss / fund.amount for fund in sorted_funds]
    real_profit_loss_values = [value * 100 for value in real_profit_loss_values]



    # Plotting
    plt.figure(figsize=(16, 9))
    plt.bar(fund_names, real_profit_loss_values, color=np.where(np.array(real_profit_loss_values) >= 0, 'green', 'red'))
    plt.xlabel("Fund")
    plt.ylabel("Profit/Loss (TL)")
    plt.title("Fund Profit/Loss")
    plt.xticks(rotation=45)
    # plt.grid(True)
    plt.yticks(np.arange(min(real_profit_loss_values), max(real_profit_loss_values), 2))


    plt.tight_layout()
    plt.show()

# def visualize_profit_ratio_by_date()
    
visualize_profit_amount_ratio()
# visualize_profit_loss()

# for fund in funds:
    # print(f"FON: {fund.fund_name} , KAR/ZARAR: {fund.profit_loss}")
