-- Create a database and a user with read privileges.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2 WITH PASSWORD 'user_0d_2_pwd';
GRANT SELECT ON DATABASE hbtn_0d_2 TO user_0d_2;