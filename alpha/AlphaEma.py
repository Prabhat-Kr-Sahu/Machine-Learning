import tradomate as tm


def strategy_info(config: tm.TradomateConfig):
    config.initial_capital = 78000
    config.ma_length1 = 100
    config.ma_length2 = 10
    config.sl_pct = 2.5  # Stop Loss in percentage
    config.tp_pct = 10
    config.qty = 100


@tm.strategy()
def my_strategy(config: tm.TradomateConfig, data: tm.TradomateData):
    # Calculate moving averages
    ma1 = tm.ta.ema(data.close, timeperiod=config.ma_length1)
    ma2 = tm.ta.ema(data.close, timeperiod=config.ma_length2)


    # Entry condition
    buy_condition = (data.close.iloc[-1] > ma1.iloc[-1]) and (data.close.iloc[-1] < ma2.iloc[-1])
    sell_condition = (data.close.iloc[-1] < ma1.iloc[-1]) and (data.close.iloc[-1] > ma2.iloc[-1])


    # Entry order
    if buy_condition:
        tm.enter_long_position_market(quantity=config.qty, comment="Long",stop_loss_percent=config.sl_pct,take_profit_percent=config.tp_pct)
    if sell_condition:
        tm.enter_short_position_market(quantity=config.qty, comment="Short",stop_loss_percent=config.sl_pct,take_profit_percent=config.tp_pct)


    # Plotting
    tm.plot(ma1, title='MA1', color='blue', overlay=True)
    tm.plot(ma2, title='MA2', color='orange', overlay=True)



