def load_data():
    import pandas as pd
    df = pd.read_csv("hn_stories.csv")
    df.columns = ["submission_time", "upvotes", "url", "headline"]
    return(df)

    if __name__ == "__main__":
        load