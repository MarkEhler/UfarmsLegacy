import formStyles from "./form.module.css";

export default function UserInfoForm() {
  return (
    <form className={formStyles.form}>
      <label htmlFor="name">
        Name: <input type="text" id="name" />
      </label>
      <label htmlFor="street">
        Street Address: <input type="text" id="street" />
      </label>
      <label htmlFor="street">
        ZIP or postal code: <input type="text" id="street" />
      </label>
      <label htmlFor="street">
        City: <input type="text" id="street" />
      </label>
      <label htmlFor="street">
        Country or Region: <input type="text" id="street" />
      </label>

      <button type="submit">Submit</button>
    </form>
  );
}
