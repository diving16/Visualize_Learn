import tushare as ts

df=ts.get_hist_data('000001',
                    start='2017-01-01',
                    end='2018-01-01').sort_index(ascending=True)

print(df)

df.high.plot()