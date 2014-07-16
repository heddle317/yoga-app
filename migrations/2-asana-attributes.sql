CREATE TABLE asana_attributes (
    "uuid" uuid NOT NULL,
    "asana_uuid" uuid NOT NULL,
    "name" varchar(500) NOT NULL,
    "value" varchar(500) NOT NULL,
    "created_at" timestamp(6) NOT NULL
);
