DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (
  id          serial     primary key,
  user_id     integer    not null,
  movie_id    integer    not null,
  rating      real       not null,
  created_at  timestamp  not null
);
