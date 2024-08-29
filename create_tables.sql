
CREATE TABLE logs (
    tstamp TIMESTAMP NOT NULL,
    level VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    query_params JSONB,
    path_params JSONB,
    session_hash VARCHAR(255),
    extra JSONB
);

 CREATE TABLE votes (
            tstamp TIMESTAMP NOT NULL,
            model_a_name VARCHAR(255) NOT NULL,
            model_b_name VARCHAR(255) NOT NULL,
            model_pair_name JSONB NOT NULL,
            chosen_model_name VARCHAR(255) NOT NULL,
            intensity VARCHAR(255),
            opening_prompt VARCHAR(255) NOT NULL,
            conversation_a JSONB NOT NULL,
            conversation_b JSONB NOT NULL,
            turns INT,
            selected_category VARCHAR(255),
            is_unedited_prompt BOOLEAN,
            template JSONB,
            uuid UUID NOT NULL,
            ip VARCHAR,
            session_hash VARCHAR,
            visitor_uuid VARCHAR,
            relevance INT,
            form INT,
            style INT,
            comments TEXT,
            extra JSONB
        );

CREATE TABLE profiles (
    tstamp TIMESTAMP NOT NULL,
    chatbot_use VARCHAR(255),
    gender VARCHAR(255),
    age VARCHAR(255),
    profession VARCHAR(255),
    session_hash VARCHAR(255),
    extra JSONB
);
