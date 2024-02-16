
        
CREATE TABLE shows
(
  id           INT          NOT NULL AUTO_INCREMENT,
  name         VARCHAR(65)  NULL    ,
  network      VARCHAR(450) NULL    ,
  release_date DATE         NULL    ,
  comments     VARCHAR(450) NULL    ,
  user_id      INT          NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45)  NULL    ,
  last_name  VARCHAR(45)  NULL    ,
  email      VARCHAR(60)  NULL    ,
  password   VARCHAR(450) NULL    ,
  created_at timestamp    NULL     DEFAULT current_timestamp,
  updated_at timestamp    NULL     DEFAULT  NULL on UPDATE current_timestamp,
  PRIMARY KEY (id)
);

ALTER TABLE shows
  ADD CONSTRAINT FK_users_TO_shows
    FOREIGN KEY (user_id)
    REFERENCES users (id);

        