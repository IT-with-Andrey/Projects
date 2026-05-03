import pytest

from logic import add_note, delet, show


@pytest.mark.parametrize(
    "title,text",
    [
        ("", "world"),
        ("hello", ""),
        ("   ", "world"),
        ("hello", "   "),
        ("", ""),
    ],
)
def test_add_note_rejects_empty_fields(title, text):
    data = {}

    with pytest.raises(ValueError):
        add_note(data, title, text)


def test_delete_string_index_should_not_crash():
    data = {
        "1": {"title": "A", "text": "B", "data": "2026-04-28 14:00"}
    }

    # Сейчас это, скорее всего, упадёт с TypeError.
    # И это хорошо: тест показывает слабое место.
    with pytest.raises(TypeError):
        delet(data, "1")


@pytest.mark.parametrize("bad_index", [0, -1, 999])
def test_delete_invalid_index_does_not_change_data(bad_index, capsys):
    data = {
        "1": {"title": "A", "text": "B", "data": "2026-04-28 14:00"}
    }

    delet(data, bad_index)

    captured = capsys.readouterr()
    assert len(data) == 1
    assert "Error" in captured.out


def test_show_empty_data_should_say_nothing_is_there(capsys):
    show({})

    captured = capsys.readouterr()
    assert "нет" in captured.out.lower() or "empty" in captured.out.lower()