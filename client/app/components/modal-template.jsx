import { useRef, useEffect } from "react";
import { createPortal } from "react-dom";
import modalStyles from "./modal.module.css";

export default function ModalTemplate({ isOpen, closeModal, children }) {
  const dialogRef = useRef();

  useEffect(() => {
    isOpen ? dialogRef.current?.showModal() : dialogRef.current?.close();
  }, [isOpen]);

  return createPortal(
    <dialog
      autofocus
      ref={dialogRef}
      onCancel={closeModal}
      className={modalStyles.modal}
    >
      {children}

      <button onClick={closeModal}>Close</button>
    </dialog>,
    document.body
  );
}
