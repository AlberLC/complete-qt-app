from PySide2 import QtGui, QtWidgets

from resources import MyStrings, url_icon


def close_dialog(controller):
    if hasattr(controller, 'dialog') and controller.dialog and controller.dialog.isVisible():
        controller.dialog.close()


def inform(title, message, text_button_accept):
    show_message(title, message, QtWidgets.QMessageBox.Information, text_button_accept)


def inform_save_successful():
    my_strings = MyStrings()
    inform(my_strings.title_save, my_strings.message_save_successful, my_strings.button_accept)


def name_empty_or_existent(name, names):
    my_strings = MyStrings()
    if not name:
        warn(my_strings.title_empty_name, my_strings.message_enter_a_name, my_strings.button_accept)
    elif name in names:
        inform(my_strings.title_existent, my_strings.message_enter_no_existent_name, my_strings.button_accept)
    else:
        return False
    return True


def name_invalid(name, names, ):
    my_strings = MyStrings()
    if name not in names:
        warn(my_strings.title_invalid, my_strings.message_enter_valid_name, my_strings.button_accept)
        return True
    return False


def question(title, message, button_accept_text, button_cancel_text):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setWindowIcon(QtGui.QIcon(QtGui.QIcon(url_icon)))
    msg_box.setIcon(QtWidgets.QMessageBox.Question)
    msg_box.setText(message)
    button_accept = QtWidgets.QPushButton(button_accept_text)
    button_reject = QtWidgets.QPushButton(button_cancel_text)
    msg_box.addButton(button_accept, QtWidgets.QMessageBox.AcceptRole)
    msg_box.addButton(button_reject, QtWidgets.QMessageBox.RejectRole)
    return msg_box.exec_()


def question_add_new_item():
    my_strings = MyStrings()
    return question(title=my_strings.title_add_new,
                    message=my_strings.message_add_new_certificate,
                    button_accept_text=my_strings.button_accept,
                    button_cancel_text=my_strings.button_cancel)


def question_delete_confirmation():
    my_strings = MyStrings()
    return question(title=my_strings.action_delete,
                    message=my_strings.message_delete_confirmation,
                    button_accept_text=my_strings.button_accept,
                    button_cancel_text=my_strings.button_cancel)


def question_delete_company_confirmation(company_names):
    my_strings = MyStrings()
    return question(title=my_strings.action_delete,
                    message=my_strings.message_delete_company_confirmation.format(f"\n{' '*8}".join(company_names)),
                    button_accept_text=my_strings.button_accept,
                    button_cancel_text=my_strings.button_cancel)


def question_exit_without_saving():
    my_strings = MyStrings()
    return question(title=my_strings.title_back,
                    message=my_strings.message_save_question,
                    button_accept_text=my_strings.button_exit_no_save,
                    button_cancel_text=my_strings.button_no_exit)


def show_message(title, message, icon_type, text_button_accept):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setWindowIcon(QtGui.QIcon(url_icon))
    msg_box.setIcon(icon_type)
    msg_box.setText(message)
    button_accept = QtWidgets.QPushButton(text_button_accept)
    msg_box.addButton(button_accept, QtWidgets.QMessageBox.AcceptRole)
    msg_box.exec_()


def warn(title, message, text_button_accept):
    show_message(title, message, QtWidgets.QMessageBox.Warning, text_button_accept)


def warn_critical(title, message, text_button_accept):
    show_message(title, message, QtWidgets.QMessageBox.Critical, text_button_accept)


def warn_critical_save_error():
    my_strings = MyStrings()
    warn_critical(my_strings.title_error, my_strings.message_save_error, my_strings.button_accept)
