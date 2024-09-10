create table category
(
    codename varchar(255) primary key,
    name     varchar(255),
    aliases  text
);

create table expense
(
    expense_id        integer primary key,
    owner   integer,
    amount            integer,
    created           DATE,
    category_codename integer,
    raw_text          text,
    FOREIGN KEY (category_codename) REFERENCES category (codename),
    foreign key (owner) REFERENCES user (telegram_id)
);

create table profit
(
    profit_id integer primary key ,
    owner integer,
    amount integer,
    created DATE,
    row_text text,
    foreign key (owner) REFERENCES user(telegram_id)
);

create table user
(
    user_id     integer primary key,
    telegram_id integer NOT NULL,
    name        varchar(255),
    fk_expenses integer,
    foreign key (fk_expenses) REFERENCES expense (expense_id)
);

insert into category (codename, name, aliases)
values ("products", "продукти", "їда, продукти"),
       ("coffee", "кава", "кава"),
       ("cafe", "кафе", "ресторан, мак, макдональдс, макдак, kfc"),
       ("transport", "громадський транспорт", "метро, автобус,тролейбус, трамвай, фонікулер, маршрутка"),
       ("taxi", "таксі", "таксі"),
       ("phone", "телефон", "телефон, звязок, рахунок, київстар, водафон, лайф, 4g"),
       ("utilities", "комунальні послуги",
        "комуналка, комунальні послуги, світло, рахунки, газ, вода, хородна вода, гаряча вода, тепло, опалення, домофон, квартплата"),
       ("pets", "домашні тварини", "собака, домашні тварини, корм, ветеренарка, вет клініка, кіт"),
       ("other", "інше", "");


