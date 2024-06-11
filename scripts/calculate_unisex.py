def most_popular_name_and_count(df):
    # Filter DataFrame for 'Mannelijk' and 'Vrouwelijk', and calculate total counts
    mannelijk_df = df[df['geslacht'] == 'Mannelijk']
    vrouwelijk_df = df[df['geslacht'] == 'Vrouwelijk']

    # Find the most popular name and count for 'Mannelijk' and 'Vrouwelijk'
    mannelijk_name = mannelijk_df.loc[mannelijk_df['aantal'].idxmax(), 'naam']
    mannelijk_count = mannelijk_df['aantal'].max()
    vrouwelijk_name = vrouwelijk_df.loc[vrouwelijk_df['aantal'].idxmax(), 'naam']
    vrouwelijk_count = vrouwelijk_df['aantal'].max()

    # Calculate the sum of counts for the most popular names across genders
    total_count = mannelijk_count + vrouwelijk_count

    # Print the most popular name and count for 'Mannelijk', 'Vrouwelijk', and the total count
    print("Populairste echte unisex naam bij de mannen:", mannelijk_name, "; Aantal:", mannelijk_count)
    print("Populairste echte unisex naam bij de vrouwen:", vrouwelijk_name, "; Aantal:", vrouwelijk_count)
    print("Populairste unisex naam in het algemeen:", total_count)
