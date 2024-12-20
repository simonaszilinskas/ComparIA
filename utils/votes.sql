
-- CREATE TABLE
--     old_votes (
--         tstamp TIMESTAMP NOT NULL,
--         model_a_name VARCHAR(255) NOT NULL,
--         model_b_name VARCHAR(255) NOT NULL,
--         model_pair_name JSONB NOT NULL,
--         chosen_model_name VARCHAR(255),
--         both_equal BOOLEAN NOT NULL,
--         opening_prompt text NOT NULL,
--         conversation_a JSONB NOT NULL,
--         conversation_b JSONB NOT NULL,
--         turns INT,
--         selected_category VARCHAR(255),
--         is_unedited_prompt BOOLEAN,
--         template JSONB,
--         uuid VARCHAR NOT NULL,
--         ip VARCHAR(255),
--         session_hash VARCHAR(255),
--         visitor_uuid VARCHAR(255),
--         details_a_positive VARCHAR(500),
--         details_a_negative VARCHAR(500),
--         details_b_positive VARCHAR(500),
--         details_b_negative VARCHAR(500),
--         comments_a TEXT,
--         comments_b TEXT,
--         extra JSONB
--     );
CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -- Timestamp of the vote
    model_a_name VARCHAR(500) NOT NULL,
    model_b_name VARCHAR(500) NOT NULL,
    model_pair_name TEXT ARRAY[2],
    chosen_model_name VARCHAR(500),
    opening_msg text NOT NULL,
    -- both_equal BOOLEAN NOT NULL,
    conversation_a JSONB NOT NULL,
    conversation_b JSONB NOT NULL,
    conv_turns INT,
    template JSONB,
    selected_category VARCHAR(255),
    is_unedited_prompt BOOLEAN,
    conversation_pair_id VARCHAR NOT NULL,
    session_hash VARCHAR(255),
    visitor_id VARCHAR(255),
    ip VARCHAR(255),
    conv_comments_a TEXT,
    conv_comments_b TEXT,
    conv_useful_a BOOLEAN,
    conv_useful_b BOOLEAN,
    conv_creative_a BOOLEAN,
    conv_creative_b BOOLEAN,
    conv_clear_formatting_a BOOLEAN,
    conv_clear_formatting_b BOOLEAN,
    conv_incorrect_a BOOLEAN,
    conv_incorrect_b BOOLEAN,
    conv_superficial_a BOOLEAN,
    conv_superficial_b BOOLEAN,
    conv_instructions_not_followed_a BOOLEAN,
    conv_instructions_not_followed_b BOOLEAN
);


-- Don't forget to add rights on sequences
GRANT USAGE, SELECT ON SEQUENCE votes_id_seq TO "languia-dev";

GRANT USAGE,
SELECT
    ON SEQUENCE votes_id_seq TO "languia-stg";

GRANT USAGE,
SELECT
    ON SEQUENCE votes_id_seq TO "languia-ro-stg";

GRANT SELECT ON TABLE votes TO "languia-ro-stg";

GRANT ALL PRIVILEGES ON TABLE votes TO "languia-stg";