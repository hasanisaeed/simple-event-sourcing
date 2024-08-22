CREATE MATERIALIZED VIEW user_balance AS
SELECT
    user_id,
    SUM(CASE WHEN event_type = 'deposit' THEN amount ELSE 0 END) -
    SUM(CASE WHEN event_type = 'withdrawal' THEN amount ELSE 0 END) AS balance
FROM events
GROUP BY user_id;
