CREATE TABLE pie
(
  id           INT          NOT NULL AUTO_INCREMENT,
  created_at   timestamp    NULL     DEFAULT current_timestamp,
  updated_at   timestamp    NULL     DEFAULT NULL on UPDATE current_timestamp,
  name         VARCHAR(65)  NULL    ,
  ingredients  VARCHAR(450) NULL    ,
  size         VARCHAR(45)  NULL    ,
  user_id      INT          NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE user
(
  id         INT          NOT NULL AUTO_INCREMENT,
  created_at timestamp    NULL     DEFAULT current_timestamp,
  updated_at timestamp    NULL     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  first_name VARCHAR(45)  NULL    ,
  last_name  VARCHAR(45)  NULL    ,
  email      VARCHAR(60)  NULL    ,
  password   VARCHAR(450) NULL    ,
  PRIMARY KEY (id)
);

ALTER TABLE pie
  ADD CONSTRAINT FK_user_TO_pie
    FOREIGN KEY (user_id)
    REFERENCES user (id);

        
