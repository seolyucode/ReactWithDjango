const tom = { lang: "Python" };
tom.lang = "Javascript";
tom["lang"] = "Ruby";

console.log(tom["lang"]);
console.log(tom);
