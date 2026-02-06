use pyo3::prelude::*;

pub mod buscal;
use buscal::{BusdayConvention, BusinessCalendar};

/// A Python module implemented in Rust.
#[pymodule]
fn rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<BusinessCalendar>()?;
    m.add_class::<BusdayConvention>()?;
    Ok(())
}
