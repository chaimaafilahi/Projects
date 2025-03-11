# unique method for extracting files
import pandas as pd

7
def readfile():
    is_valid = False
    df = pd.DataFrame()
    while not is_valid:
        path = input("Insert file path: ")
        try:
            df = pd.read_csv(path)
        except FileNotFoundError as fe:
            print(f"ERROR: {fe}")
        except Exception as e:
            print(f"ERROR: {e}")
        else:
            is_valid = True
            print("Path entered correctly!")
    else:
        return df

def percentual_loading(df, cur, sql):
    # eseguo la query per caricare i dati (il risultato del caricamento è in percentuale)
    print(f"Loading... {str(len(df))} row to insert.")
    perc_int = 0
    for index, row in df.iterrows():
        perc = float("%.2f" % ((index + 1) / len(df) * 100))
        if perc >= perc_int:
            print(f"{round(perc)}% Completed")
            perc_int += 5
        cur.execute(sql, row.to_list())

def bar_load(df,cur,sql):
    print(f"Loading... \n{str(len(df))} row to insert.")
    print("┌──────────────────────────────────────────────────┐")
    print("│",end="")
    perc_int = 2
    for index, row in df.iterrows():
        perc = float("%.2f" % ((index + 1) / len(df) * 100))
        if perc >= perc_int:
            print("█",end="")
            perc_int += 2
        cur.execute(sql, row.to_list())
    print("│ 100% Completed!")
    print("└──────────────────────────────────────────────────┘")

if __name__ =="__main__":
    readfile()
