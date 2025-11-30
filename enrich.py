import csv
import yfinance as yf
import time

input_file = "halal_stocks.csv"
output_file = "halal_stocks_debug.csv"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", newline="", encoding="utf-8") as fout:

    reader = csv.reader(fin)
    writer = csv.writer(fout)

    header = next(reader)
    writer.writerow(header + ["used_symbol", "ltp", "pe", "market_cap", "status"])

    for i, row in enumerate(reader):

        base = row[1].strip()   # COL2 locked
        candidates = [base + ".NS", base + ".BO"]

        print("\n---")
        print("Base symbol:", base)
        if not base:
            continue

        ltp = pe = mcap = ""
        status = "fail"
        used = ""

        for sym in candidates:
            print("Trying:", sym)

            try:
                stock = yf.Ticker(sym)
                info = stock.info

                ltp = info.get("regularMarketPrice")
                pe = info.get("trailingPE")
                mcap = info.get("marketCap")

                if ltp or mcap:
                    print("OK:", ltp, pe, mcap)
                    status = "ok"
                    used = sym
                    break
                else:
                    print("NO DATA FIELDS")

            except Exception as e:
                print("ERROR:", str(e))

            # time.sleep(0.6)

        writer.writerow(row + [used, ltp or "", pe or "", mcap or "", status])