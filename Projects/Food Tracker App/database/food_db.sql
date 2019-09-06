create table log_date (
    id integer primary key autoincrement,
    entre_date date no null
);

create table food(
    id integer primary key autoincrement,
    name_food text not null,
    protein integer not null,
    carbohydrates integer not null,
    fat integer not null,
    calories integer not null
);

create table food_log(
    food_id integer not null,
    log_data_id integer not null,
    primary key(food_id,log_data_id)
);

