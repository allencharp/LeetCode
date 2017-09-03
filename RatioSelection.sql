-- Given a Student table, write a SQL query to find male ratio
--
-- +---------+-------------+
-- | Id(INT) | Name  | Sex |
-- +---------+-------------+
-- |       1 | Judy  |  F  |
-- |       2 | Peter |  M  |
-- |       3 | Allen |  M  |
-- |       4 | Wood  |  M  |
-- +---------+-------------+
-- For example, return the following Ids for the above Weather table:
-- +------+
-- | male |
-- +------+
-- | 0.75 |
-- +------+
-- Subscribe to see which companies asked this question

SELECT sum(case when `Sex` = 'M' then 1 else 0 end)/count(*) as male,
       sum(case when `Sex` = 'F' then 1 else 0 end)/count(*) as female
FROM Student