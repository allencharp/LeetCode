-- Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
-- 
-- +---------+------------+------------------+
-- | Id(INT) | Date(DATE) | Temperature(INT) |
-- +---------+------------+------------------+
-- |       1 | 2015-01-01 |               10 |
-- |       2 | 2015-01-02 |               25 |
-- |       3 | 2015-01-03 |               20 |
-- |       4 | 2015-01-04 |               30 |
-- +---------+------------+------------------+
-- For example, return the following Ids for the above Weather table:
-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+
-- Subscribe to see which companies asked this question

select w1.id from weather w1 Inner JOIN weather w2 on subdate(w1.date, 1) = date(w2.date)
where w1.temperature > w2.temperature

