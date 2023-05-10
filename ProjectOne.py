import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('championsdata.csv')

# Select columns 0 to 2 and column 17 using iloc
new_df = df.iloc[:, list(range(2)) +[3] + [17]][df['Win']==1]

# Select columns 0 to 2 and column 17 using iloc
new_df_Two = df.iloc[:, list(range(2)) +[3] + [17]][df['Win']==0]

print(new_df)
print(new_df_Two)

# Add the totals of Wins
Win_total = (new_df['Win'] == 1).sum()

# Add the total of times the finals winners didnt win a game in the series
Loss_total = (new_df_Two['Win']==0).sum()

# Add the totals of rebounds for games won
Rebound_total = new_df['TRB'].sum()

# Add the totals of rebounds for games lossed
Rebound_total_Two = new_df_Two['TRB'].sum()

# Stores number of rows in variable
number_of_rows = len(new_df)

# Stores number of rows in variable
number_of_rows_Two = len(new_df_Two)

# Calculate average rebounds for games won and lossed
Average_Rebounds = Rebound_total/number_of_rows
Average_Rebounds_Two = Rebound_total_Two/number_of_rows_Two



pd.set_option('display.max_columns', None)


# Create a new DataFrame to store the results
results_df = pd.DataFrame({
    'Win Total': [Win_total],
    'Loss Total': [Loss_total],
    'Rebounds for Games Won': [Rebound_total],
    'Rebounds for Games Lost': [Rebound_total_Two],
    'Av Rebounds for Games Won': [Average_Rebounds],
    'Av Rebounds for Games Lost': [Average_Rebounds_Two]
})

print(results_df)

# Export the results to a CSV file
results_df.to_csv('PythonProject1_results.csv', index=False)
