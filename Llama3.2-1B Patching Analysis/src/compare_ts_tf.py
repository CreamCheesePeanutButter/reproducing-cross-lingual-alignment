import json
from pathlib import Path

FOLDER = Path(__file__).resolve().parent.parent / 'data'

def readFile(file_path):
    if file_path is None:
        return []
    
    data = []

    with open(file_path, 'r', encoding = 'utf-8') as file:
        for line in file:
            data.append(json.loads(line))

    return data


def compare(file_path_1, file_path_2):
    # Read both files
    data1 = readFile(file_path_1)
    data2 = readFile(file_path_2)

    # Number of successes
    succ1 = 0
    succ2 = 0

    # Transfer failures and successes
    ts = 0
    tf = 0

    count = 0

    # Go through all results
    for result1, result2 in zip(data1, data2):
        # Confirm same index
        if result1['idx'] != result2['idx']:
            continue

        # Count total accuracy
        if result1['acc'] > 0.0:
            succ1 += 1
        if result2['acc'] > 0.0:
            succ2 += 1

        # Transfer success and failure, assumes english as first language
        if result1['acc'] > 0.0 and result2['acc'] > 0.0:
            ts += 1
        elif result1['acc'] > 0.0 and not result2['acc'] > 0.0:
            tf += 1

        count += 1

    # Accuracy is the number of successes divided by total count
    acc1 = succ1 / count
    acc2 = succ2 / count

    print(f"{str(file_path_1)}\nvs.\n{str(file_path_2)}")
    print("-----")
    print(f"Data points compared: {count}")
    print(f"Total successes #1: {succ1}")
    print(f"Total successes #2: {succ2}")
    print(f"Accuracy #1: {acc1*100:.1f}%")
    print(f"Accuracy #2: {acc2*100:.1f}%")
    print(f"TS / TF: {ts} / {tf}")
    print("")

    return

# File names
belebele_english = 'belebele_eval_Llama3.2-1B_eng_Latn_ABCD.jsonl'
belebele_french = 'belebele_eval_Llama3.2-1B_fra_Latn_ABCD.jsonl'
belebele_german = 'belebele_eval_Llama3.2-1B_deu_Latn_ABCD.jsonl'
belebele_hindi = 'belebele_eval_Llama3.2-1B_hin_Deva_ABCD.jsonl'
belebele_italian = 'belebele_eval_Llama3.2-1B_ita_Latn_ABCD.jsonl'
belebele_portuguese = 'belebele_eval_Llama3.2-1B_por_Latn_ABCD.jsonl'
belebele_spanish = 'belebele_eval_Llama3.2-1B_spa_Latn_ABCD.jsonl'
#belebele_thai = None

xcopa_english_italian = 'xcopa_eval_Llama3.2-1B_translation-it_AB.jsonl'
xcopa_italian = 'xcopa_eval_Llama3.2-1B_it_AB.jsonl'
xcopa_english_thai = 'xcopa_eval_Llama3.2-1B_translation-th_AB.jsonl'
xcopa_thai = 'xcopa_eval_Llama3.2-1B_th_AB.jsonl'
# TODO: add english-italian and english-thai for xcopa

xstorycloze_english = 'xstorycloze_eval_Llama3.2-1B_en_AB.jsonl'
xstorycloze_spanish = 'xstorycloze_eval_Llama3.2-1B_es_AB.jsonl'
xstorycloze_hindi = 'xstorycloze_eval_Llama3.2-1B_hi_AB.jsonl'

# English with other languages
compare(FOLDER / belebele_english, FOLDER / belebele_french)
compare(FOLDER / belebele_english, FOLDER / belebele_german)
compare(FOLDER / belebele_english, FOLDER / belebele_hindi)
compare(FOLDER / belebele_english, FOLDER / belebele_italian)
compare(FOLDER / belebele_english, FOLDER / belebele_portuguese)
compare(FOLDER / belebele_english, FOLDER / belebele_spanish)
#compare(FOLDER / belebele_english, FOLDER / belebele_thai)

compare(FOLDER / xcopa_english_italian, FOLDER / xcopa_italian)
compare(FOLDER / xcopa_english_thai, FOLDER / xcopa_thai)

compare(FOLDER / xstorycloze_english, FOLDER / xstorycloze_spanish)
compare(FOLDER / xstorycloze_english, FOLDER / xstorycloze_hindi)