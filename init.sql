create table coins
(
    name text,
    ticker text,
    link text,
    created_at timestamp without time zone default CURRENT_TIMESTAMP,
    CONSTRAINT link UNIQUE (link)
);
