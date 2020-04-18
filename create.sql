REM   Script: create
REM   creating tables

create table winner( 
      winner_name varchar(50) not null PRIMARY KEY 
);

create table top_scorer( 
      top_scorer_name varchar(50) not null PRIMARY KEY, 
      club VARCHAR(50) NOT NULL, 
      goals integer DEFAULT NULL 
);

create table season( 
      season_index integer DEFAULT NULL PRIMARY KEY, 
      season_year integer DEFAULT NULL, 
      winner_name VARCHAR(50) NOT NULL REFERENCES winner(winner_name), 
      top_scorer_name VARCHAR(50) NOT NULL REFERENCES top_scorer(top_scorer_name) 
);

