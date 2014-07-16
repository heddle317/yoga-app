CREATE TABLE asana_images (
    "uuid" uuid NOT NULL,
    "asana_uuid" uuid NOT NULL,
    "primary_image" BOOLEAN NOT NULL,
    "image_url" varchar(500) NOT NULL,
    "created_at" timestamp(6) NOT NULL
);
