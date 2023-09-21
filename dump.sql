--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin;

--
-- Name: book; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.book (
    title character varying(255),
    author character varying(255) NOT NULL,
    genre character varying(100) NOT NULL,
    quantity integer NOT NULL,
    uuid uuid NOT NULL
);


ALTER TABLE public.book OWNER TO admin;

--
-- Name: rental_book; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.rental_book (
    uuid_user uuid,
    uuid_book uuid,
    is_read boolean NOT NULL,
    uuid uuid NOT NULL
);


ALTER TABLE public.rental_book OWNER TO admin;

--
-- Name: user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."user" (
    name character varying(255) NOT NULL,
    uuid uuid NOT NULL
);


ALTER TABLE public."user" OWNER TO admin;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.alembic_version (version_num) FROM stdin;
bb5304475cfc
\.


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.book (title, author, genre, quantity, uuid) FROM stdin;
ноа	марк леви	проза	4	a0101213-7366-46fa-b5b3-f716241e7df1
плащ для красной шапочки	кэтрин кей	фентези	2	c3ea07bf-2ade-4839-9a4f-2506813ce9c7
стеклянный трон	сара маас	фентези	1	2db1190b-b086-46f4-860c-bf56ce0f724a
иностранка	сергей довлатов	проза	5	8e374aec-f3a8-4622-94d0-f302967becf0
аватар короля	худе лань	манга	2	f0ec6675-459a-448c-a097-4334024695f4
феномены мозга	владимир бехтерев	психология	6	e8ce6aa6-397b-4eb2-8754-b9b00537975f
робототехника	сергей мельников	наука	2	8383ba9b-705d-4a5f-be10-e3c610c0b912
\.


--
-- Data for Name: rental_book; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.rental_book (uuid_user, uuid_book, is_read, uuid) FROM stdin;
d569cdd9-85d5-4150-99e7-b7ee59c06b89	8e374aec-f3a8-4622-94d0-f302967becf0	f	f6c6320d-57be-47be-abe2-2b61af756ea2
d1133485-fffd-48ee-8bf6-cdc7ed6b197f	f0ec6675-459a-448c-a097-4334024695f4	f	b3dfe6d3-9f90-4d15-8e8f-53af5b4926ac
547975f6-4ac4-47e7-8921-a8546ab89b5a	2db1190b-b086-46f4-860c-bf56ce0f724a	f	775f24e3-6f6d-4ff7-b55a-e49b54fd8ac5
547975f6-4ac4-47e7-8921-a8546ab89b5a	f0ec6675-459a-448c-a097-4334024695f4	f	abd7d3ed-26cb-4b4e-94ac-417693ba2d90
d1133485-fffd-48ee-8bf6-cdc7ed6b197f	8e374aec-f3a8-4622-94d0-f302967becf0	t	e10d36fc-ced9-490d-80b3-7103a1af8b9a
547975f6-4ac4-47e7-8921-a8546ab89b5a	a0101213-7366-46fa-b5b3-f716241e7df1	t	72daaac8-3dfb-4122-833a-24564ee9e381
547975f6-4ac4-47e7-8921-a8546ab89b5a	c3ea07bf-2ade-4839-9a4f-2506813ce9c7	t	83f908ac-3601-4a42-abf8-10ef76f10f31
2f5b70ab-de25-4feb-a03c-23217ce293ab	a0101213-7366-46fa-b5b3-f716241e7df1	t	d27c8e3a-8048-4041-b8c9-08165765d58b
2f5b70ab-de25-4feb-a03c-23217ce293ab	e8ce6aa6-397b-4eb2-8754-b9b00537975f	t	44c71ccf-8760-462f-82a9-2933e25aaf08
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."user" (name, uuid) FROM stdin;
пользователь 1	d1133485-fffd-48ee-8bf6-cdc7ed6b197f
ибрагим ибрагимович	d569cdd9-85d5-4150-99e7-b7ee59c06b89
анна владимировна	2f5b70ab-de25-4feb-a03c-23217ce293ab
кто-нибудь еще	547975f6-4ac4-47e7-8921-a8546ab89b5a
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (uuid);


--
-- Name: book book_title_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_title_key UNIQUE (title);


--
-- Name: rental_book rental_book_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.rental_book
    ADD CONSTRAINT rental_book_pkey PRIMARY KEY (uuid);


--
-- Name: user user_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_name_key UNIQUE (name);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (uuid);


--
-- Name: rental_book rental_book_uuid_book_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.rental_book
    ADD CONSTRAINT rental_book_uuid_book_fkey FOREIGN KEY (uuid_book) REFERENCES public.book(uuid);


--
-- Name: rental_book rental_book_uuid_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.rental_book
    ADD CONSTRAINT rental_book_uuid_user_fkey FOREIGN KEY (uuid_user) REFERENCES public."user"(uuid) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

