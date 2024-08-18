--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

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
-- Name: common_auth_account_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.common_auth_account_1_1 (
    deleted boolean,
    detail text,
    display_name text,
    email text,
    external_id text,
    family_name text,
    given_name text,
    id text NOT NULL,
    org text,
    owner text,
    policy text,
    sref text,
    tstamp integer,
    uref text,
    username text
);


ALTER TABLE public.common_auth_account_1_1 OWNER TO system;

--
-- Name: common_auth_group_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.common_auth_group_1_1 (
    deleted boolean,
    description text,
    display_name text,
    external_id text,
    id text NOT NULL,
    name text,
    org text,
    owner text,
    parent_id text,
    sref text,
    tstamp integer,
    uref text
);


ALTER TABLE public.common_auth_group_1_1 OWNER TO system;

--
-- Name: common_auth_org_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.common_auth_org_1_1 (
    deleted boolean,
    display_name text,
    external_id text,
    id text NOT NULL,
    name text,
    org text,
    owner text,
    sref text,
    tstamp integer,
    uref text
);


ALTER TABLE public.common_auth_org_1_1 OWNER TO system;

--
-- Name: common_auth_policy_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.common_auth_policy_1_1 (
    acl_create text,
    acl_delete text,
    acl_read text,
    acl_update text,
    deleted boolean,
    description text,
    display_name text,
    external_id text,
    id text NOT NULL,
    name text,
    org text,
    owner text,
    sref text,
    tstamp integer,
    uref text
);


ALTER TABLE public.common_auth_policy_1_1 OWNER TO system;

--
-- Name: demo_device_cart_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.demo_device_cart_1_1 (
    deleted boolean,
    description text,
    display_name text,
    id text NOT NULL,
    is_battery_alert boolean,
    is_person_alert boolean,
    is_warning boolean,
    location text,
    manager text,
    name text,
    org text,
    owner text,
    round_id text,
    sref text,
    tstamp integer,
    type text,
    uref text
);


ALTER TABLE public.demo_device_cart_1_1 OWNER TO system;

--
-- Name: demo_operation_round_1_1; Type: TABLE; Schema: public; Owner: system
--

CREATE TABLE public.demo_operation_round_1_1 (
    cart_id_list text,
    current_hole text,
    deleted boolean,
    description text,
    display_name text,
    half text,
    id text NOT NULL,
    is_nine_hole_plus boolean,
    is_vip boolean,
    name text,
    org text,
    owner text,
    round_order text,
    sref text,
    tstamp integer,
    uref text
);


ALTER TABLE public.demo_operation_round_1_1 OWNER TO system;

--
-- Data for Name: common_auth_account_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.common_auth_account_1_1 (deleted, detail, display_name, email, external_id, family_name, given_name, id, org, owner, policy, sref, tstamp, uref, username) FROM stdin;
f	{"id":"00000000-0000-0000-0000-000000000000","sref":"","uref":""}	system	system@trinity.eqpls.net	3cfdf439-43ae-4a05-92bb-91b21e51875f	system	system	25d47889-384d-4725-a940-4a5f4fec14a8	trinity		["admin"]	common.auth.Account	1723960956	/uerp/v1/common/auth/account/25d47889-384d-4725-a940-4a5f4fec14a8	system
f	{"id":"00000000-0000-0000-0000-000000000000","sref":"","uref":""}	admin	admin@trinity.eqpls.net	b567b53c-d19d-4f3d-86f1-97adcb08a81a	admin	admin	8c73ba29-de51-4abb-9d0f-ca897ba1c55b	trinity		["admin","user"]	common.auth.Account	1723960956	/uerp/v1/common/auth/account/8c73ba29-de51-4abb-9d0f-ca897ba1c55b	admin
\.


--
-- Data for Name: common_auth_group_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.common_auth_group_1_1 (deleted, description, display_name, external_id, id, name, org, owner, parent_id, sref, tstamp, uref) FROM stdin;
\.


--
-- Data for Name: common_auth_org_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.common_auth_org_1_1 (deleted, display_name, external_id, id, name, org, owner, sref, tstamp, uref) FROM stdin;
f	Trinity	3e86a831-4ccf-4722-9065-d2dd9db60009	eff2787f-8e0b-43db-84f5-c003e5e67a22	trinity	trinity		common.auth.Org	1723960955	/uerp/v1/common/auth/org/eff2787f-8e0b-43db-84f5-c003e5e67a22
\.


--
-- Data for Name: common_auth_policy_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.common_auth_policy_1_1 (acl_create, acl_delete, acl_read, acl_update, deleted, description, display_name, external_id, id, name, org, owner, sref, tstamp, uref) FROM stdin;
[]	[]	[]	[]	f			e3d9ab8a-e005-40cd-b582-7448e5e0f53e	ff1c5dac-2c63-4527-9651-68fbbd4af298	admin	trinity		common.auth.Policy	1723960956	/uerp/v1/common/auth/policy/ff1c5dac-2c63-4527-9651-68fbbd4af298
[]	[]	[]	[]	f			1318ca48-a1bb-4383-9d2b-0b139b52d13f	84139631-5e9c-4615-b102-33500649d11f	user	trinity		common.auth.Policy	1723960956	/uerp/v1/common/auth/policy/84139631-5e9c-4615-b102-33500649d11f
\.


--
-- Data for Name: demo_device_cart_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.demo_device_cart_1_1 (deleted, description, display_name, id, is_battery_alert, is_person_alert, is_warning, location, manager, name, org, owner, round_id, sref, tstamp, type, uref) FROM stdin;
f			dfe20d99-1a36-4fcb-bbf5-deb2042475be	t	f	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	555	trinity	admin		demo.device.Cart	1723961181	work	/uerp/v1/demo/device/cart/dfe20d99-1a36-4fcb-bbf5-deb2042475be
f			ddcadf44-cb1b-4b23-899b-9981b4352df4	t	f	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	666	trinity	admin		demo.device.Cart	1723961181	waiting	/uerp/v1/demo/device/cart/ddcadf44-cb1b-4b23-899b-9981b4352df4
f			0644e5d3-c201-421f-8e41-6a421c2091db	f	t	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	777	trinity	admin		demo.device.Cart	1723961181	training	/uerp/v1/demo/device/cart/0644e5d3-c201-421f-8e41-6a421c2091db
f			35a21b5a-eef7-419f-b5c0-d9cde336094c	f	f	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	123	trinity	admin	c7fa1131-053a-4895-8c12-20e4e4435a2a	demo.device.Cart	1723961187	round	/uerp/v1/demo/device/cart/35a21b5a-eef7-419f-b5c0-d9cde336094c
f			f1cb013c-cda1-481c-b28a-e16c78e232b1	f	f	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	456	trinity	admin	3f0652b4-26d7-4bdd-9cfa-61b426b3121c	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/f1cb013c-cda1-481c-b28a-e16c78e232b1
f			2b198249-c22a-465e-828f-1b69981c8646	t	f	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	789	trinity	admin	c4676c2d-590f-4f6d-988d-38dc19c4817e	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/2b198249-c22a-465e-828f-1b69981c8646
f			6e4c1d59-b21b-47ae-95e1-a8370df3f247	t	f	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	112	trinity	admin	4cb0939f-416a-487c-877d-c5758ff149d4	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/6e4c1d59-b21b-47ae-95e1-a8370df3f247
f			acf582c4-43e1-411c-8f83-73136cd3377f	f	t	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	135	trinity	admin	93cfce56-06a3-4fcd-a962-c445ccb6e6da	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/acf582c4-43e1-411c-8f83-73136cd3377f
f			89b9c017-a32c-4d55-88a7-6f8d6b659a22	f	t	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	718	trinity	admin	11b3c5e2-86bd-4942-a208-f6eb1762bdc4	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/89b9c017-a32c-4d55-88a7-6f8d6b659a22
f			dab3d376-ffb3-40b3-af4b-79645a4e0cc1	t	t	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	191	trinity	admin	9ba72c6c-011e-4fa3-aae3-460f892077d1	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/dab3d376-ffb3-40b3-af4b-79645a4e0cc1
f			c718e42e-71ec-4a05-92cd-4cd622736af4	t	t	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	222	trinity	admin	05a0f01d-b499-4553-935d-c8218982bab9	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/c718e42e-71ec-4a05-92cd-4cd622736af4
f			fd07fd1d-0d09-484a-87ba-3f47f56ed460	f	f	f	{"x":37.5665,"y":126.978}	{"name":"\\uae40\\ucca0\\uc218","type":"caddy"}	333	trinity	admin	a99463dc-8a4c-4e35-9d11-6698bb2e8c91	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/fd07fd1d-0d09-484a-87ba-3f47f56ed460
f			15345774-fc30-4851-ac90-08c1845da813	f	f	t	{"x":37.5665,"y":126.978}	{"name":"\\ud64d\\uae38\\ub3d9","type":"caddy"}	444	trinity	admin	b9ae9a6f-a6f3-4ec2-9815-4a5e922825fe	demo.device.Cart	1723961188	round	/uerp/v1/demo/device/cart/15345774-fc30-4851-ac90-08c1845da813
\.


--
-- Data for Name: demo_operation_round_1_1; Type: TABLE DATA; Schema: public; Owner: system
--

COPY public.demo_operation_round_1_1 (cart_id_list, current_hole, deleted, description, display_name, half, id, is_nine_hole_plus, is_vip, name, org, owner, round_order, sref, tstamp, uref) FROM stdin;
["35a21b5a-eef7-419f-b5c0-d9cde336094c"]	{"number":9,"courseType":"out","startTime":"12:00","elapsedTime":"00:30","scheduledEndTime":"12:30"}	f			first	c7fa1131-053a-4895-8c12-20e4e4435a2a	f	f	ROUND 1	trinity	admin		demo.operation.Round	1723961187	/uerp/v1/demo/operation/round/c7fa1131-053a-4895-8c12-20e4e4435a2a
["f1cb013c-cda1-481c-b28a-e16c78e232b1"]	{"number":10,"courseType":"in","startTime":"12:30","elapsedTime":"01:00","scheduledEndTime":"13:30"}	f			second	3f0652b4-26d7-4bdd-9cfa-61b426b3121c	t	t	ROUND 2	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/3f0652b4-26d7-4bdd-9cfa-61b426b3121c
["2b198249-c22a-465e-828f-1b69981c8646"]	{"number":4,"courseType":"out","startTime":"13:30","elapsedTime":"00:30","scheduledEndTime":"14:00"}	f			first	c4676c2d-590f-4f6d-988d-38dc19c4817e	f	f	ROUND 3	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/c4676c2d-590f-4f6d-988d-38dc19c4817e
["6e4c1d59-b21b-47ae-95e1-a8370df3f247"]	{"number":18,"courseType":"in","startTime":"14:00","elapsedTime":"00:30","scheduledEndTime":"14:30"}	f			second	4cb0939f-416a-487c-877d-c5758ff149d4	t	t	ROUND 4	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/4cb0939f-416a-487c-877d-c5758ff149d4
["acf582c4-43e1-411c-8f83-73136cd3377f"]	{"number":9,"courseType":"out","startTime":"14:30","elapsedTime":"00:30","scheduledEndTime":"15:00"}	f			first	93cfce56-06a3-4fcd-a962-c445ccb6e6da	f	f	ROUND 5	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/93cfce56-06a3-4fcd-a962-c445ccb6e6da
["89b9c017-a32c-4d55-88a7-6f8d6b659a22"]	{"number":10,"courseType":"in","startTime":"15:00","elapsedTime":"00:30","scheduledEndTime":"15:30"}	f			second	11b3c5e2-86bd-4942-a208-f6eb1762bdc4	t	t	ROUND 6	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/11b3c5e2-86bd-4942-a208-f6eb1762bdc4
["dab3d376-ffb3-40b3-af4b-79645a4e0cc1"]	{"number":4,"courseType":"out","startTime":"15:30","elapsedTime":"00:30","scheduledEndTime":"16:00"}	f			first	9ba72c6c-011e-4fa3-aae3-460f892077d1	f	f	ROUND 7	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/9ba72c6c-011e-4fa3-aae3-460f892077d1
["c718e42e-71ec-4a05-92cd-4cd622736af4"]	{"number":18,"courseType":"in","startTime":"16:00","elapsedTime":"00:30","scheduledEndTime":"16:30"}	f			second	05a0f01d-b499-4553-935d-c8218982bab9	t	t	ROUND 8	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/05a0f01d-b499-4553-935d-c8218982bab9
["fd07fd1d-0d09-484a-87ba-3f47f56ed460"]	{"number":9,"courseType":"out","startTime":"16:30","elapsedTime":"00:30","scheduledEndTime":"17:00"}	f			first	a99463dc-8a4c-4e35-9d11-6698bb2e8c91	f	f	ROUND 9	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/a99463dc-8a4c-4e35-9d11-6698bb2e8c91
["15345774-fc30-4851-ac90-08c1845da813"]	{"number":10,"courseType":"in","startTime":"17:00","elapsedTime":"00:30","scheduledEndTime":"17:30"}	f			second	b9ae9a6f-a6f3-4ec2-9815-4a5e922825fe	t	t	ROUND 10	trinity	admin		demo.operation.Round	1723961188	/uerp/v1/demo/operation/round/b9ae9a6f-a6f3-4ec2-9815-4a5e922825fe
\.


--
-- Name: common_auth_account_1_1 common_auth_account_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.common_auth_account_1_1
    ADD CONSTRAINT common_auth_account_1_1_pkey PRIMARY KEY (id);


--
-- Name: common_auth_group_1_1 common_auth_group_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.common_auth_group_1_1
    ADD CONSTRAINT common_auth_group_1_1_pkey PRIMARY KEY (id);


--
-- Name: common_auth_org_1_1 common_auth_org_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.common_auth_org_1_1
    ADD CONSTRAINT common_auth_org_1_1_pkey PRIMARY KEY (id);


--
-- Name: common_auth_policy_1_1 common_auth_policy_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.common_auth_policy_1_1
    ADD CONSTRAINT common_auth_policy_1_1_pkey PRIMARY KEY (id);


--
-- Name: demo_device_cart_1_1 demo_device_cart_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.demo_device_cart_1_1
    ADD CONSTRAINT demo_device_cart_1_1_pkey PRIMARY KEY (id);


--
-- Name: demo_operation_round_1_1 demo_operation_round_1_1_pkey; Type: CONSTRAINT; Schema: public; Owner: system
--

ALTER TABLE ONLY public.demo_operation_round_1_1
    ADD CONSTRAINT demo_operation_round_1_1_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

