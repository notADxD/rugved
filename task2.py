#1
import pandas as pd
matches_df = pd.read_csv('matches.csv')
matches_2008 = matches_df[matches_df['season'] == 2008 ]
print(matches_2008.count()[0])


#2
import pandas as pd
matches_df = pd.read_csv('matches.csv')
max_matches = matches_df['city'].value_counts().idxmax()
min_matches= matches_df['city'].value_counts().idxmin()
print(f"MOST MATCHES : {max_matches}")
print(f"LEAST MATCHES : {min_matches}")


#3
import pandas as pd
matches_df = pd.read_csv('matches.csv')
match = matches_df['city'].value_counts()
print(match)


#4
import pandas as pd
matches_df = pd.read_csv('matches.csv')
toss_max = matches_df['toss_winner'].value_counts().idxmax()
toss_min = matches_df['toss_winner'].value_counts().idxmin()
print(f"Most tosses won: {toss_max}")
print(f"Least tosses won: {toss_min}")


#5
import pandas as pd
matches_df = pd.read_csv('matches.csv')
toss_max = matches_df['toss_winner'].value_counts().idxmax()
toss_min = matches_df['toss_winner'].value_counts().idxmin()
toss_max_df = matches_df[matches_df['toss_winner'] == toss_max]
toss_min_df = matches_df[matches_df['toss_winner'] == toss_min]
decision_counts_max = toss_max_df['toss_decision'].value_counts()
decision_counts_min = toss_min_df['toss_decision'].value_counts()
print(toss_max)
print(decision_counts_max)
print(toss_min)
print(decision_counts_min)


#6
import pandas as pd
matches_df = pd.read_csv('matches.csv')
result = matches_df['result'].value_counts()
print(result)


#7
import pandas as pd
matches_df = pd.read_csv('matches.csv')
tie_matches = matches_df[matches_df['result'] == 'tie']
tie_teams = tie_matches[['team1','team2']]
print(tie_teams)


#8
import pandas as pd
matches_df = pd.read_csv('matches.csv')
win_margin_df = matches_df[['winner','win_by_runs']]
print(win_margin_df.sort_values('win_by_runs').tail(1))


#9
import pandas as pd
matches_df = pd.read_csv('matches.csv')
win_margin_df = matches_df[['winner','win_by_runs']]
nonzero_win_margin_df = win_margin_df[win_margin_df['win_by_runs'] != 0]
print(nonzero_win_margin_df.sort_values('win_by_runs').head(1))


#10
import pandas as pd
matches_df = pd.read_csv('matches.csv')
potm_df = matches_df['player_of_match'].value_counts()
potm3_df = potm_df[potm_df>3]
print(potm3_df)


#11
import pandas as pd
matches_df = pd.read_csv('matches.csv')
potm = matches_df['player_of_match'].value_counts().sort_values().tail(1)
print(potm)


#12
import pandas as pd
matches_df = pd.read_csv('matches.csv')
win_venue_df = matches_df[['venue','win_by_runs']]
a = win_venue_df.sort_values('win_by_runs').tail(1)
print(a['venue'])


#13
import pandas as pd
matches_df = pd.read_csv('matches.csv')
win_venue_df = matches_df[['venue','win_by_runs']]
a = win_venue_df.sort_values('win_by_runs').head(1)
print(a['venue'])


#14
import pandas as pd
matches_df = pd.read_csv('matches.csv')
umpires =pd.concat([matches_df['umpire1'], matches_df['umpire2']])
print(umpires.value_counts().idxmax())


#15
import pandas as pd
matches_df = pd.read_csv('matches.csv')
count = 2008
while(count < 2020):
    matches_per_year = matches_df[matches_df['season'] == count ]
    print(f"matches in {count} : " )
    print(matches_per_year.count()[0])
    count += 1


#16
import pandas as pd
matches_df = pd.read_csv('matches.csv')
deliveries_df = pd.read_csv('deliveries.csv')
matches_df =matches_df.rename(columns={'id': 'match_id'})
merged_df = matches_df.merge(deliveries_df, on = "match_id")
sum_year = merged_df.groupby('season')[['total_runs']].sum()
print(sum_year)


#17
import pandas as pd
matches_df = pd.read_csv('matches.csv')
print(matches_df['toss_winner'].value_counts())


#18
import pandas as pd
matches_df = pd.read_csv('matches.csv')
sum_year = matches_df.groupby('season')[['toss_decision']].value_counts()
print(sum_year)
sum_year.plot(kind = 'bar')


#19
import pandas as pd
deliveries_df = pd.read_csv('deliveries.csv')
dismissal_kind = deliveries_df['dismissal_kind'].value_counts()
dismissal_kind.plot(kind = 'bar')


#20
import pandas as pd
deliveries_df = pd.read_csv('deliveries.csv')
score_batsman =deliveries_df.groupby('batsman')[['batsman_runs']].sum()
top_ten = score_batsman.sort_values('batsman_runs').tail(10)
top_ten.plot(kind = 'bar')


#21
import pandas as pd
matches_df = pd.read_csv('matches.csv')
potm = matches_df['player_of_match'].value_counts()
top_10_pom = potm.sort_values().tail(10)
top_10_pom.plot(kind = 'bar')


#22
import pandas as pd
matches_df = pd.read_csv('matches.csv')
a = matches_df['team1'].value_counts()
b= matches_df['team2'].value_counts()
print(a+b)


#23
import pandas as pd
matches_df = pd.read_csv('matches.csv')
a = matches_df['team1'].value_counts()
b= matches_df['team2'].value_counts()
total_matches_played = a + b
matches_won = matches_df['winner'].value_counts()
win_rate = matches_won/total_matches_played
result_df = pd.DataFrame({'Total Matches Played': total_matches_played, 'Matches Won': matches_won,'Win Rate': win_rate})
print(result_df)


#24
import pandas as pd
matches_df = pd.read_csv('matches.csv')
distribution_df = matches_df['winner'].value_counts()
distribution_df.plot(kind = 'bar')


#25
import pandas as pd
matches_df = pd.read_csv('matches.csv')
a = matches_df['team1'].value_counts()
b= matches_df['team2'].value_counts()
total_matches_played = a + b
matches_won = matches_df['winner'].value_counts()
win_rate = matches_won/total_matches_played
print(win_rate)


#26
import pandas as pd
matches_df = pd.read_csv('matches.csv')
team_decision = matches_df.groupby('toss_winner')[['toss_decision']].value_counts()
print(team_decision)
