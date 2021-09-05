import numpy
from numpy.lib.ufunclike import fix
import pandas
from pandas.io.pytables import Fixed
pandas.set_option('display.unicode.east_asian_width', True)

fixed_cost      = 100   # 工場の固定費用(万円)
run_cost        = 600   # 機械1台の稼働コスト(万円)
sale_price      = 0.2   # 製品1つの販売台数(万円)

machine_ability = 5000  # 機械1台で作られる製品数(個)
demand_boom     = 10000 # 好況時の需要量(個)
demand_slump    = 5000  # 不況時の需要量(個)

def calc_payoff_table(fixed_cost, run_cost, sale_price, 
                      machine_ability, demand_boom, demand_slump):
    # 出荷される製品の個数
    num_product_df = pandas.DataFrame({
        '0台': [0, 0],
        '1台': [min([machine_ability, demand_boom]),
                min([machine_ability, demand_slump])],
        '2台': [min([machine_ability * 2, demand_boom]),
                min([machine_ability * 2, demand_slump])]
    })

    # 売上行列
    sales_df = num_product_df * sale_price

    # 製造コスト
    run_cost_df = pandas.DataFrame({
        '0台': numpy.repeat(fixed_cost               , 2),
        '1台': numpy.repeat(fixed_cost + run_cost    , 2),
        '2台': numpy.repeat(fixed_cost + run_cost * 2, 2)
    })

    # 利得行列
    payoff_df = sales_df - run_cost_df
    payoff_df.index = ['好況', '不況']
    return payoff_df

payoff = calc_payoff_table(fixed_cost=100, run_cost=600, sale_price=0.2, 
                           machine_ability=5000, demand_boom=10000,
                           demand_slump=5000)
#print(payoff)

# 最大値をとるインデックスを取得する。最大値が複数ある場合はすべて出力する
def argmax_list(series):
    return (list(series[series == series.max()].index))

# 最小値をとるインデックスを取得する。最小値が複数ある場合はすべて出力する
def argmin_list(series):
    return (list(series[series == series.min()].index))

print('Maximax: ', argmax_list(payoff.max()))
print('Maximin: ', argmax_list(payoff.min()))
