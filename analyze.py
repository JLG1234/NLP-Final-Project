# %%
import pandas as pd

# Load CSV file
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

df = load_csv("data.csv")

# Raw labels array
# labels = df["label_text"].unique().tolist()
labels = ['alarm_set', 'audio_volume_mute', 'iot_hue_lightchange', 'iot_hue_lightoff', 'iot_hue_lightdim', 'iot_cleaning', 'calendar_query', 'play_music', 'general_quirky', 'general_greet', 'datetime_query', 'datetime_convert', 'takeaway_query', 'alarm_remove', 'alarm_query', 'news_query', 'music_likeness', 'music_query', 'iot_hue_lightup', 'takeaway_order', 'weather_query', 'music_settings', 'general_joke', 'music_dislikeness', 'audio_volume_other', 'iot_coffee', 'audio_volume_up', 'iot_wemo_on', 'iot_hue_lighton', 'iot_wemo_off', 'audio_volume_down', 'qa_stock', 'play_radio', 'recommendation_locations', 'qa_factoid', 'calendar_set', 'play_audiobook', 'play_podcasts', 'social_query', 'transport_query', 'email_sendemail', 'recommendation_movies', 'lists_query', 'play_game', 'transport_ticket', 'recommendation_events', 'email_query', 'transport_traffic', 'cooking_query', 'qa_definition', 'calendar_remove', 'lists_remove', 'cooking_recipe', 'email_querycontact', 'lists_createoradd', 'transport_taxi', 'qa_maths', 'social_post', 'qa_currency', 'email_addcontact']

# Define label groups
intent_groups = {
    "alarms_and_time": [
        'alarm_set', 'alarm_remove', 'alarm_query',
        'datetime_query', 'datetime_convert',
        'calendar_query', 'calendar_set', 'calendar_remove'
    ],
    "music_and_audio": [
        'play_music', 'music_query', 'music_likeness', 'music_dislikeness', 'music_settings',
        'audio_volume_mute', 'audio_volume_up', 'audio_volume_down', 'audio_volume_other',
        'play_radio', 'play_audiobook', 'play_podcasts'
    ],
    "iot_and_smart_home": [
        'iot_hue_lightchange', 'iot_hue_lighton', 'iot_hue_lightoff', 'iot_hue_lightup', 'iot_hue_lightdim',
        'iot_wemo_on', 'iot_wemo_off', 'iot_cleaning', 'iot_coffee'
    ],
    "recommendations": [
        'recommendation_movies', 'recommendation_events', 'recommendation_locations'
    ],
    "communication": [
        'email_sendemail', 'email_query', 'email_querycontact', 'email_addcontact',
        'social_post', 'social_query'
    ],
    "qa_and_knowledge": [
        'qa_factoid', 'qa_definition', 'qa_maths', 'qa_stock', 'qa_currency'
    ],
    "lists_and_tasks": [
        'lists_createoradd', 'lists_query', 'lists_remove'
    ],
    "food": [
        'takeaway_query', 'takeaway_order', 'cooking_query', 'cooking_recipe'
    ],
    "transport": [
        'transport_query', 'transport_ticket', 'transport_traffic', 'transport_taxi'
    ],
    "general_chitchat": [
        'general_quirky', 'general_greet', 'general_joke', 'play_game'
    ],
    "weather_and_news": [
        'weather_query', 'news_query'
    ]
}

# Create a dictionary of DataFrames grouped by intent
grouped_dfs = {}
for group_name, label_list in intent_groups.items():
    grouped_dfs[group_name] = df[df["label_text"].isin(label_list)].reset_index(drop=True)

# Example usage: preview a group
# print(grouped_dfs["music_and_audio"].head())

# You can also save them as separate CSVs if needed:
# for group, gdf in grouped_dfs.items():
#     gdf.to_csv(f"{group}.csv", index=False)

# %%