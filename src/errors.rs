#[cfg(feature = "python")]
use pyo3::{exceptions::*, prelude::PyErr};

#[cfg(feature = "python")]
pub(crate) fn py_err_from_serde(err: serde_json::Error) -> PyErr {
    if err.is_data() {
        PyValueError::new_err("Bad/malformed data")
    } else if err.is_eof() {
        PyEOFError::new_err("Unexpectedly reached end of JSON data.")
    } else if err.is_io() {
        PyIOError::new_err("An I/O error occurred parsing JSON file.")
    } else if err.is_syntax() {
        PyValueError::new_err("Bad JSON syntax.")
    } else {
        PyException::new_err("An unspecified error occurred")
    }
}
