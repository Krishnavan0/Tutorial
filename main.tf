variable "myvariable" {
    type = string
    default = "welcome to terraform"
}

variable "mapvariable" {
    type = map(string)
    default = {
        new_key = "new_variable"
    }
}