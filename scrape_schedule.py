import json, pandas as pd
def main(args=None):
    with open("hs.json", "r", encoding="utf-8") as f:
        data = json.load(f)["data"]
    df = pd.DataFrame(data)
    df.to_csv("latest_data.csv", index=False)
if __name__ == "__main__": main()
