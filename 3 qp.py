import pandas as pd
dataset = {
    "job_title": ['Software Engineer', 'Data Scientist', 'Product Manager', 'Marketing Manager', 'Sales Manager'],
    "department": ['Engineering', 'Data Science', 'Product', 'Marketing', 'Sales']
}

df = pd.DataFrame(dataset)

df = df.sort_values(by=['job_title'], ascending=False)
print(df)
