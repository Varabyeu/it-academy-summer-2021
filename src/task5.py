    pupil1_langs = ['Russian', 'English']
    pupil2_langs = ['Russian', 'Belarusian', 'English']
    pupil3_langs = ['Russian', 'Italian', 'French']
    pupil_all_langs = set(pupil1_langs + pupil2_langs + pupil3_langs)
    print("Языки, которые знают ученики: ")
    for langs in pupil_all_langs:
        print(langs)
    set_p1 = set(pupil1_langs)
    set_p2 = set(pupil2_langs)
    set_p3 = set(pupil3_langs)
    one_more_lang = set_p1 & set_p2 & set_p3
    print("Языки, которые знает хотя бы один из школьников: ")
    for lang in one_more_lang:
        print(lang)
