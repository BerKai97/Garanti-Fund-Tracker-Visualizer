from models import Fund
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from qbstyles import mpl_style
# from ing_theme_matplotlib import mpl_style


def get_funds_of_file(fund_file: str):
    with open(fund_file, encoding="utf-8") as f:
        json_data = json.load(f)

    funds: list[Fund] = []
    for fund in json_data:
        funds.append(Fund(fund))
    return funds


def get_funds_from_folder(folder: str):
    funds: dict[str, list[Fund]] = {}
    for file in os.listdir(folder):
        funds[file.split(".")[0]] = get_funds_of_file(os.path.join(folder, file))
    return funds


# Visualize profit/loss
def visualize_profit_loss(file=None):
    if file is None:
        lastest_file = max(
            [os.path.join("datas", file) for file in os.listdir("datas")],
            key=os.path.getctime,
        )
        funds = get_funds_of_file(lastest_file)
    else:
        funds = get_funds_of_file(file)

    sorted_funds = sorted(funds, key=lambda fund: fund.profit_loss, reverse=True)

    fund_names = [fund.fund_name for fund in sorted_funds]
    profit_loss_values = [fund.profit_loss for fund in sorted_funds]

    # Plotting
    plt.figure(figsize=(16, 9))
    plt.bar(
        fund_names,
        profit_loss_values,
        color=np.where(np.array(profit_loss_values) >= 0, "green", "red"),
    )
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


def visualize_profit_amount_ratio(file=None):
    if file is None:
        lastest_file = max(
            [os.path.join("datas", file) for file in os.listdir("datas")],
            key=os.path.getctime,
        )
        funds = get_funds_of_file(lastest_file)
    else:
        funds = get_funds_of_file(file)
    sorted_funds = sorted(
        funds, key=lambda fund: fund.profit_loss / fund.amount, reverse=True
    )

    fund_names = [fund.fund_name for fund in sorted_funds]
    real_profit_loss_values = [fund.profit_loss / fund.amount for fund in sorted_funds]
    real_profit_loss_values = [value * 100 for value in real_profit_loss_values]

    # Plotting
    plt.figure(figsize=(16, 9))
    plt.bar(
        fund_names,
        real_profit_loss_values,
        color=np.where(np.array(real_profit_loss_values) >= 0, "green", "red"),
    )
    plt.xlabel("Fund")
    plt.ylabel("Profit/Loss (TL)")
    plt.title("Fund Profit/Loss")
    plt.xticks(rotation=45)
    # plt.grid(True)
    plt.yticks(np.arange(min(real_profit_loss_values), max(real_profit_loss_values), 2))

    plt.tight_layout()
    plt.show()


def visualize_profit_loss_by_date(funds_by_date):
    dates = list(funds_by_date.keys())
    sorted_dates = sorted(dates)

    fund_names_by_date = {}
    profit_loss_values_by_date = {}

    all_funds = set()

    for date in sorted_dates:
        funds: list[Fund] = funds_by_date[date]
        sorted_funds = sorted(
            funds, key=lambda fund: fund.fund_name
        )  # Sort by fund name
        fund_names = [fund.fund_name for fund in sorted_funds]
        real_profit_loss_values = []

        for fund in sorted_funds:
            if fund.amount != 0:
                real_profit_loss_values.append(fund.profit_loss)
            else:
                real_profit_loss_values.append(0)

        fund_names_by_date[date] = fund_names
        profit_loss_values_by_date[date] = real_profit_loss_values

        all_funds.update(fund_names)  # Collect all fund names

    # Ensure all funds have a corresponding value for each date
    for date in sorted_dates:
        missing_funds = all_funds - set(fund_names_by_date[date])
        for fund in missing_funds:
            if fund in fund_names_by_date[sorted_dates[-1]]:
                index = fund_names_by_date[sorted_dates[-1]].index(fund)
                profit_loss_values_by_date[date].insert(index, 0)
            else:
                profit_loss_values_by_date[date].append(0)
                fund_names_by_date[sorted_dates[-1]].append(fund)

    # Plotting
    plt.figure(figsize=(16, 9))
    bar_width = 0.15
    num_dates = len(sorted_dates)
    num_funds = len(fund_names_by_date[sorted_dates[-1]])
    index = np.arange(num_funds)

    for i, date in enumerate(sorted_dates):
        plt.bar(
            index + i * bar_width,
            profit_loss_values_by_date[date],
            bar_width,
            color="C" + str(i),
        )

    plt.grid(False)
    plt.xlabel("Fund")
    plt.ylabel("Profit/Loss (TL)")
    plt.title("Fund Profit/Loss by Date")
    plt.xticks(
        index + (num_dates - 1) * bar_width / 2,
        fund_names_by_date[sorted_dates[-1]],
        rotation=45,
    )

    average_profit_loss = [
        np.sum(profit_loss_values_by_date[date]) for date in sorted_dates
    ]
    plt.legend(
        [
            f"Date: {date}, Total Profit/Loss: {average_profit_loss[i]:.2f}"
            for i, date in enumerate(sorted_dates)
        ]
    )
    plt.tight_layout()
    plt.show()



def visualize_profit_amount_ratio_by_date(funds_by_date):
    dates = list(funds_by_date.keys())
    sorted_dates = sorted(dates)

    fund_names_by_date = {}
    real_profit_loss_values_by_date = {}

    all_funds = set()

    for date in sorted_dates:
        funds: list[Fund] = funds_by_date[date]
        sorted_funds = sorted(
            funds, key=lambda fund: fund.fund_name
        )  # Sort by fund name
        fund_names = [fund.fund_name for fund in sorted_funds]
        real_profit_loss_values = []

        for fund in sorted_funds:
            if fund.amount != 0:
                real_profit_loss_values.append(fund.profit_loss / fund.amount * 100)
            else:
                real_profit_loss_values.append(0)

        fund_names_by_date[date] = fund_names
        real_profit_loss_values_by_date[date] = real_profit_loss_values

        all_funds.update(fund_names)  # Collect all fund names

    # Ensure all funds have a corresponding value for each date
    for date in sorted_dates:
        missing_funds = all_funds - set(fund_names_by_date[date])
        for fund in missing_funds:
            if fund in fund_names_by_date[sorted_dates[-1]]:
                index = fund_names_by_date[sorted_dates[-1]].index(fund)
                real_profit_loss_values_by_date[date].insert(index, 0)
            else:
                real_profit_loss_values_by_date[date].append(0)
                fund_names_by_date[sorted_dates[-1]].append(fund)

    # Plotting
    plt.figure(figsize=(16, 9))
    bar_width = 0.15
    num_dates = len(sorted_dates)
    num_funds = len(fund_names_by_date[sorted_dates[-1]])
    index = np.arange(num_funds)

    for i, date in enumerate(sorted_dates):
        plt.bar(
            index + i * bar_width,
            real_profit_loss_values_by_date[date],
            bar_width,
            color="C" + str(i),
        )

    plt.grid(False)
    plt.xlabel("Fund")
    plt.ylabel("Profit/Loss (%)")
    plt.title("Fund Profit/Loss by Date")
    plt.xticks(
        index + (num_dates - 1) * bar_width / 2,
        fund_names_by_date[sorted_dates[-1]],
        rotation=45,
    )

    average_profit_loss = [
        np.average(real_profit_loss_values_by_date[date]) for date in sorted_dates
    ]
    plt.legend(
        [
            f"Date: {date}, Total Profit/Loss: {average_profit_loss[i]:.2f} %"
            for i, date in enumerate(sorted_dates)
        ]
    )
    plt.tight_layout()
    plt.show()




funds_by_date = get_funds_from_folder("datas")
visualize_profit_loss_by_date(funds_by_date)
# visualize_profit_amount_ratio_by_date(funds_by_date)

# visualize_profit_amount_ratio()
# visualize_profit_loss("datas/17-7-2023.json")


# for k,v in get_funds_from_folder("datas").items():
#     print(k)
#     for fund in v:
#         print(fund.fund_name, fund.profit_loss)
#     print("-----")


# for fund in funds:
# print(f"FON: {fund.fund_name} , KAR/ZARAR: {fund.profit_loss}")
