from typing import List

import keyboard


CONTINUE_KEYS = ["[", "]"]  # keys that play/advance one step
EXIT_KEY = "="  # key that stops the script


# Edit this sheet directly in code.
SHEET_TEXT = """
[8wtsfj]jkk[uosk]klkkkhh
[59wdj]jkk[ryok]klkkkhh
[G269dj]jkk[Qeyk]klkkkhh
[370fj]jkk[wruk]klkkkhh
[8wtpsj][pj][ak][ak][uoask][ak][sl][ak][ak][ak][8wtoh][oh]
[59wpdj][pj][ak][ak][ryoak][ak][sl][ak][ak][ak][59woh][oh]
[269pdj][pj][ak][ak][Qeyak][ak][sl][ak][ak][ak][269oh][oh]
[G269pdj]69QeyIpdGj[dz]-[29]-
[18]58[0wyo][8p][wa][tuoa]w0[8yo][5p][1a]
[5rya]2567[79wyod]-59[wo][9o]
[I29yp]690Q[QIeyd]-26[9o][6I]
[30eI]7[0wu]Qwr[upG]r[wof]Q0[3ah]
[18]58[0wyo][8p][wa][tuoa]w0[8yo][5p][1a]
[5rya]2567[79wyod]-59[wo][9o]
[I29yp]690Q[eypQIG]-26[9uf][6IG]
[30pIG]7[0uf][pQIG]wr[upIG]r[wuof][Quof]0[3y]
[18tup]58[0wup]8w[tup][wa]0[8y][5y][1y]
[5ryp]25[79yp]59[wyp][9oa]7[5yo]25
[I29yp]6[I9p]0[QIp]e[Iyp]e[QIp]0[I9p]2
[I30p]7[0uoa]Qwr[upG]r[wof][Qyd][0yd]3
[18psj]58[0wpsj]8w[tpsj]w0[8yd][5yd]1
[5pdj]25[79pdj]59[wpdj][9ak]7[5yd]25
[G29pj]6[G9pj]0[QGpj]e[Gypj]e[Qoh]0[9IG]2
[30pIG]7[0uof]Q[wd][rf][uoaf][roaf][woaf][Qoaf]03
[18uof]58[0wosh]8w[0wtsfl]-[8adk]51
[5wyod]9w[ryodh]wy[ryofhx]-[wdhz]95
[29pIG]69[Qepdj]9e[QGeydz]-[G9sl]6[G2sl]
[30]7[0afk]Qwr[uI][ro][wa][Qf][0G][3h]
[18of][5u][8of][0wsh][8o][wsh][tfl][ws][0fl][8dk][5a][1dk]
[5od][2y][5od][79dh][5o][9dh][whx][9f][7hx][5hz][2d][5hz]
[29pG][6I][9pG][Qedj][9p][edj][Geydz]9[ey][Iyd]GjpzzC[Gj]bz----
[ak]-[ak]-[fx]-
[18fhx]58[0wfhx]8w[tfhx]w[0ak][8ak]5[1dz]
[G29dz]69[Qepdj]9e[Gydz][Gedz][QGdz][G9dz][6sfl][2sfl]
[5wsfl]9[wadk]erw[$QGdz][G9dz][QGdz][Gedz][9sfl][Qsfl]
[30sfl]7[0adk]w70[29pdj]6[9adk]Q[6odh]9
[18fhx]58[0wfhx]8w[thlv]w[0GC][8fhx]5[1dz]
[G29dz]69[Qepdj]9e[Gydz][Gedz][QGdz][G9dz][6sfl][2sfl]
[5wsfl]9[wadk]erw[$QGdz][G9dz][QGdz][Gedz][9sfl][Qsfl]
[30sfl]7[0adk]w70[29pdj]6[9adk]Q[6odh]9
[18uof]58[0wosh]8w[tsfl]w0[8adk]51
[I29yd]69[epQIG]9e[yfhx]eQ[G9dz]62
[5woah]9w[radk]9w[$Qjzb]9Q[ejGC]9[Qhkv]
[30]7[0fhx]Qwr[uI][ro][wa][Qf][0G][3h]
[18of][5u][8of][0wsh][8o][wsh][tfl][ws][0fl][8dk][5a][1dk]
[I29d][6y][I9d][epQG][9I][epG][yjx][eG][Qjx][G9z][6d][G2z]
[5wah][9o][wah][rdk][9a][wdk][$Qzb][9j][Qzb][ejC][9d][Qhkv]
[30]70Qw[rfhx]uIoafG
h----w w 
[370rup]-o-o [yI]-I-I-
[269ey]-u y-r r-
[269eu]--y r-r-r-
[1580w]----w w 
[370rup]-o-Q [wyI]-I0I-
[269eyI]-u y [Qe] r r u 
[269eu]--[0y]y[Qy]-[9r]-[2r]-
[1580wr]----
[1580]-w-t-[18r]58
[269]-Q-u-[29y]69
[$7r]-y-[Q9ryp]-I-[ro]
[370]-u-3737[0I]Qw
[18tu]-[1o]58[0wtus]-[8a]15
[29ey]-[2yI]69[QIeyf]-[I9d]26
[I7ya]$7[9Q]7[QIya][Irya]Q9[I7yd]$2
[I7yd]$79Qr[Iyhkv]-[7GC]7[$fx]
[18fhx]58[0wfhx]8w[tfhx]w[0ak][8ak]5[1dz]
[G29dz]69[Qepdj]9e[Gydz][Gedz][QGdz][G9dz][6sfl][2sfl]
[5wsfl]9[wadk]erw[$QGdz][G9dz][QGdz][Gedz][9sfl][Qsfl]
[30sfl]7[0adk]w70[29pdj]6[9adk]Q[6odh]9
[18fhx]58[0wfhx]8w[thlv]w[0GC][8fhx]5[1dz]
[G29dz]69[Qepdj]9e[Gydz][Gedz][QGdz][G9dz][6sfl][2sfl]
[5wsfl]9[wadk]erw[$QGdz][G9dz][QGdz][Gedz][9sfl][Qsfl]
[30sfl]7[0adk]w70[29pdj]6[9adk]Q[6odh]9
[18uof]58[0wosh]8w[tsfl]w0[8adk]51
[I29yd]69[epQIG]9e[yfhx]eQ[G9dz]62
[5woah]9w[radk]9w[$Qjzb]9Q[ejGC]9[Qhkv]
[30]7[0fhx]Qwr[uI][ro][wa][Qf][0G][3h]
[18of][5u][8of][0wsh][8o][wsh][tfl][ws][0fl][8dk][5a][1dk]
[I29d][6y][I9d][epQG][9I][epG][yjx][eG][Qjx][G9z][6d][G2z]
[5wah][9o][wah][rdk][9a][wdk][$Qzb][9j][Qzb][ejC][9d][Qhkv]
[30]7[0fhx]Qwr[udz]r[wdz]Q[0pj]3
[18psj][5psj][8psj][0wpsj][8psj][wpsj][tpsj]w[0adk]85[1oah]
[29odh][6pdj][9pdj][Qepdj][9pdj][epdj][yIG]eQ[G9sl]62
[5odh][2pdj][5pdj][79pdj][5pdj][9pdj][wpdj]9[7adk]52[5oah]
[30odh][7pdj][0pdj][wrpdj][0pdj][rpdj]ur[wpj][0pj]7[3oh]
[18of][5u][8of][0wsh][8o][wsh][tfl][ws][0fl][8dk][5a][1dk]
[I29d][6y][I9d][epQG][9I][epG][yjx][eG][Qjx][G9z][6d][G2z]
[5wah][9o][wah][rdk][9a][wdk][$Qzb][9j][Qzb][ejC][9d][Qhkv]
[30]70QwruIo[fhx]-
[8wtsfj]jkk[uosk]klkkkhh
[59wdj]jkk[ryok]klkkkhh
[G269dj]jkk[Qeyk]klkkkhh
[370fj]jkk[wruk]klkkkhh
[8wtpj][pj][ak][ak][uoask][ak][sl][ak][ak][ak][8wtoh][oh]
[59wpj][pj][ak][ak][ryoak][ak][sl][ak][ak][ak][59woh][oh]
[269pj][pj][ak][ak][Qeyak][ak][sl][ak][ak][ak][269oh][oh]
[G269pdj]-hGdpoIyewQ962
""" # replace sheets with your own sheets








# DO NOT EDIT BELOW IF YOU DONT KNOW WHAT YOU ARE DOING

SHIFTED_SYMBOL_TO_BASE = {
    "~": "`",
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
    "_": "-",
    "+": "=",
    "{": "[",
    "}": "]",
    "|": "\\",
    ":": ";",
    '"': "'",
    "<": ",",
    ">": ".",
}


def parse_sheet(sheet: str) -> List[List[str]]:
    """
    Parse sheet text into steps.

    Rules:
    - Anything inside [] or {} is a chord (pressed together).
    - Outside groups, each visible character is one step (e.g. jkk -> j, k, k).
    - Spaces and '-' are treated as separators.
    """
    normalized = sheet.replace("-", " ")
    steps: List[List[str]] = []

    i = 0
    n = len(normalized)

    while i < n:
        ch = normalized[i]

        if ch.isspace():
            i += 1
            continue

        if ch in "[{":
            closing = "]" if ch == "[" else "}"
            end = normalized.find(closing, i + 1)
            if end == -1:
                # No closing bracket found; treat the opener as a normal token.
                token = ch.strip()
                if token:
                    steps.append([token])
                i += 1
                continue

            group_text = normalized[i + 1 : end]
            compact = "".join(group_text.split())

            # If group has no spaces, interpret each character as one key:
            # [Qwap] -> Q, w, a, p pressed together
            if compact:
                chord_keys = [c for c in compact]
                steps.append(chord_keys)

            i = end + 1
            continue

        # Parse plain run outside groups
        j = i
        while j < n and (not normalized[j].isspace()) and normalized[j] not in "[{]}":
            j += 1

        token = normalized[i:j]
        for c in token:
            if not c.isspace():
                steps.append([c])
        i = j

    return steps


def play_step(keys: List[str]) -> None:
    """Press all keys in `keys` together (or single if only one)."""
    if not keys:
        return

    resolved = []
    for k in keys:
        needs_shift = False
        base_key = k
        if len(k) == 1 and k.isalpha() and k.isupper():
            needs_shift = True
            base_key = k.lower()
        elif len(k) == 1 and k in SHIFTED_SYMBOL_TO_BASE:
            needs_shift = True
            base_key = SHIFTED_SYMBOL_TO_BASE[k]
        resolved.append((base_key, needs_shift))

    if len(resolved) == 1:
        key, needs_shift = resolved[0]
        if needs_shift:
            keyboard.press("shift")
            keyboard.press(key)
            keyboard.release(key)
            keyboard.release("shift")
        else:
            keyboard.press_and_release(key)
        return

    unshifted = [base for base, needs_shift in resolved if not needs_shift]
    shifted = [base for base, needs_shift in resolved if needs_shift]

    # For mixed chords, hold unshifted keys first, then add shifted keys with Shift.
    for k in unshifted:
        keyboard.press(k)

    if shifted:
        keyboard.press("shift")
        for k in shifted:
            keyboard.press(k)

    for k in reversed(shifted):
        keyboard.release(k)
    if shifted:
        keyboard.release("shift")
    for k in reversed(unshifted):
        keyboard.release(k)


def main() -> None:
    print("Virtual Piano Autoplayer (step-by-step)")
    print("- Groups in [] or {} are chords.")
    print("- Space-separated tokens outside groups are singles.")
    print("- '-' acts like a separator/space.")
    print()

    sheet = SHEET_TEXT.strip()
    if not sheet:
        print("SHEET_TEXT is empty. Exiting.")
        return

    continue_keys = [k.strip().lower() for k in CONTINUE_KEYS if k and k.strip()]
    exit_key = EXIT_KEY.strip().lower()
    if not continue_keys:
        print("CONTINUE_KEYS is empty. Exiting.")
        return
    if not exit_key:
        print("EXIT_KEY is empty. Exiting.")
        return

    steps = parse_sheet(sheet)
    if not steps:
        print("No playable steps found after parsing. Exiting.")
        return

    print(f"\nParsed {len(steps)} steps.")
    print(f"Press {continue_keys} to play next step, '{exit_key}' to quit.")
    print("Waiting for input...\n")

    state = {
        "index": 0,
        "pressed": set(),  # prevents key-repeat while a trigger key is held
    }

    def on_continue_press(_event) -> None:
        key_name = _event.name
        if key_name in state["pressed"]:
            return

        state["pressed"].add(key_name)
        idx = state["index"]

        if idx >= len(steps):
            print("Sheet complete.")
            return

        current = steps[idx]
        print(f"Step {idx + 1}/{len(steps)} -> {current}")
        play_step(current)
        state["index"] += 1

    def on_continue_release(_event) -> None:
        key_name = _event.name
        state["pressed"].discard(key_name)

    for key in continue_keys:
        keyboard.on_press_key(key, on_continue_press, suppress=False)
        keyboard.on_release_key(key, on_continue_release, suppress=False)

    keyboard.wait(exit_key)
    print("Exited.")


if __name__ == "__main__":
    main()
