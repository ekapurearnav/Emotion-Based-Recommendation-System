<?php

namespace App\Http\services;

abstract class AbstractTokenizer
{
    static protected $pattern = '';

    public function getPattern()
    {
        if (empty(static::$pattern)) {
            throw new \LogicException("Tokenizer must define split \$pattern value");
        } else {
            return static::$pattern;
        }
    }
}
