function validateForm() {
    const income = Number(document.querySelector('[name="applicant_income"]').value);
    const loan = Number(document.querySelector('[name="loan_amount"]').value);
    if (income < 0 || loan <= 0) {
        alert("Please enter valid income and loan amount.");
        return false;
    }
    return true;
}
